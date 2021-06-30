// Copyright 2021 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.25.0
// 	protoc        v3.13.0
// source: google/type/calendar_period.proto

package calendarperiod

import (
	proto "github.com/golang/protobuf/proto"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// This is a compile-time assertion that a sufficiently up-to-date version
// of the legacy proto package is being used.
const _ = proto.ProtoPackageIsVersion4

// A `CalendarPeriod` represents the abstract concept of a time period that has
// a canonical start. Grammatically, "the start of the current
// `CalendarPeriod`." All calendar times begin at midnight UTC.
type CalendarPeriod int32

const (
	// Undefined period, raises an error.
	CalendarPeriod_CALENDAR_PERIOD_UNSPECIFIED CalendarPeriod = 0
	// A day.
	CalendarPeriod_DAY CalendarPeriod = 1
	// A week. Weeks begin on Monday, following
	// [ISO 8601](https://en.wikipedia.org/wiki/ISO_week_date).
	CalendarPeriod_WEEK CalendarPeriod = 2
	// A fortnight. The first calendar fortnight of the year begins at the start
	// of week 1 according to
	// [ISO 8601](https://en.wikipedia.org/wiki/ISO_week_date).
	CalendarPeriod_FORTNIGHT CalendarPeriod = 3
	// A month.
	CalendarPeriod_MONTH CalendarPeriod = 4
	// A quarter. Quarters start on dates 1-Jan, 1-Apr, 1-Jul, and 1-Oct of each
	// year.
	CalendarPeriod_QUARTER CalendarPeriod = 5
	// A half-year. Half-years start on dates 1-Jan and 1-Jul.
	CalendarPeriod_HALF CalendarPeriod = 6
	// A year.
	CalendarPeriod_YEAR CalendarPeriod = 7
)

// Enum value maps for CalendarPeriod.
var (
	CalendarPeriod_name = map[int32]string{
		0: "CALENDAR_PERIOD_UNSPECIFIED",
		1: "DAY",
		2: "WEEK",
		3: "FORTNIGHT",
		4: "MONTH",
		5: "QUARTER",
		6: "HALF",
		7: "YEAR",
	}
	CalendarPeriod_value = map[string]int32{
		"CALENDAR_PERIOD_UNSPECIFIED": 0,
		"DAY":                         1,
		"WEEK":                        2,
		"FORTNIGHT":                   3,
		"MONTH":                       4,
		"QUARTER":                     5,
		"HALF":                        6,
		"YEAR":                        7,
	}
)

func (x CalendarPeriod) Enum() *CalendarPeriod {
	p := new(CalendarPeriod)
	*p = x
	return p
}

func (x CalendarPeriod) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (CalendarPeriod) Descriptor() protoreflect.EnumDescriptor {
	return file_google_type_calendar_period_proto_enumTypes[0].Descriptor()
}

func (CalendarPeriod) Type() protoreflect.EnumType {
	return &file_google_type_calendar_period_proto_enumTypes[0]
}

func (x CalendarPeriod) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use CalendarPeriod.Descriptor instead.
func (CalendarPeriod) EnumDescriptor() ([]byte, []int) {
	return file_google_type_calendar_period_proto_rawDescGZIP(), []int{0}
}

var File_google_type_calendar_period_proto protoreflect.FileDescriptor

var file_google_type_calendar_period_proto_rawDesc = []byte{
	0x0a, 0x21, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2f, 0x74, 0x79, 0x70, 0x65, 0x2f, 0x63, 0x61,
	0x6c, 0x65, 0x6e, 0x64, 0x61, 0x72, 0x5f, 0x70, 0x65, 0x72, 0x69, 0x6f, 0x64, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x12, 0x0b, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e, 0x74, 0x79, 0x70, 0x65,
	0x2a, 0x7f, 0x0a, 0x0e, 0x43, 0x61, 0x6c, 0x65, 0x6e, 0x64, 0x61, 0x72, 0x50, 0x65, 0x72, 0x69,
	0x6f, 0x64, 0x12, 0x1f, 0x0a, 0x1b, 0x43, 0x41, 0x4c, 0x45, 0x4e, 0x44, 0x41, 0x52, 0x5f, 0x50,
	0x45, 0x52, 0x49, 0x4f, 0x44, 0x5f, 0x55, 0x4e, 0x53, 0x50, 0x45, 0x43, 0x49, 0x46, 0x49, 0x45,
	0x44, 0x10, 0x00, 0x12, 0x07, 0x0a, 0x03, 0x44, 0x41, 0x59, 0x10, 0x01, 0x12, 0x08, 0x0a, 0x04,
	0x57, 0x45, 0x45, 0x4b, 0x10, 0x02, 0x12, 0x0d, 0x0a, 0x09, 0x46, 0x4f, 0x52, 0x54, 0x4e, 0x49,
	0x47, 0x48, 0x54, 0x10, 0x03, 0x12, 0x09, 0x0a, 0x05, 0x4d, 0x4f, 0x4e, 0x54, 0x48, 0x10, 0x04,
	0x12, 0x0b, 0x0a, 0x07, 0x51, 0x55, 0x41, 0x52, 0x54, 0x45, 0x52, 0x10, 0x05, 0x12, 0x08, 0x0a,
	0x04, 0x48, 0x41, 0x4c, 0x46, 0x10, 0x06, 0x12, 0x08, 0x0a, 0x04, 0x59, 0x45, 0x41, 0x52, 0x10,
	0x07, 0x42, 0x78, 0x0a, 0x0f, 0x63, 0x6f, 0x6d, 0x2e, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x2e,
	0x74, 0x79, 0x70, 0x65, 0x42, 0x13, 0x43, 0x61, 0x6c, 0x65, 0x6e, 0x64, 0x61, 0x72, 0x50, 0x65,
	0x72, 0x69, 0x6f, 0x64, 0x50, 0x72, 0x6f, 0x74, 0x6f, 0x50, 0x01, 0x5a, 0x48, 0x67, 0x6f, 0x6f,
	0x67, 0x6c, 0x65, 0x2e, 0x67, 0x6f, 0x6c, 0x61, 0x6e, 0x67, 0x2e, 0x6f, 0x72, 0x67, 0x2f, 0x67,
	0x65, 0x6e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2f, 0x67, 0x6f, 0x6f, 0x67, 0x6c, 0x65, 0x61, 0x70,
	0x69, 0x73, 0x2f, 0x74, 0x79, 0x70, 0x65, 0x2f, 0x63, 0x61, 0x6c, 0x65, 0x6e, 0x64, 0x61, 0x72,
	0x70, 0x65, 0x72, 0x69, 0x6f, 0x64, 0x3b, 0x63, 0x61, 0x6c, 0x65, 0x6e, 0x64, 0x61, 0x72, 0x70,
	0x65, 0x72, 0x69, 0x6f, 0x64, 0xa2, 0x02, 0x03, 0x47, 0x54, 0x50, 0x62, 0x06, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x33,
}

var (
	file_google_type_calendar_period_proto_rawDescOnce sync.Once
	file_google_type_calendar_period_proto_rawDescData = file_google_type_calendar_period_proto_rawDesc
)

func file_google_type_calendar_period_proto_rawDescGZIP() []byte {
	file_google_type_calendar_period_proto_rawDescOnce.Do(func() {
		file_google_type_calendar_period_proto_rawDescData = protoimpl.X.CompressGZIP(file_google_type_calendar_period_proto_rawDescData)
	})
	return file_google_type_calendar_period_proto_rawDescData
}

var file_google_type_calendar_period_proto_enumTypes = make([]protoimpl.EnumInfo, 1)
var file_google_type_calendar_period_proto_goTypes = []interface{}{
	(CalendarPeriod)(0), // 0: google.type.CalendarPeriod
}
var file_google_type_calendar_period_proto_depIdxs = []int32{
	0, // [0:0] is the sub-list for method output_type
	0, // [0:0] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_google_type_calendar_period_proto_init() }
func file_google_type_calendar_period_proto_init() {
	if File_google_type_calendar_period_proto != nil {
		return
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_google_type_calendar_period_proto_rawDesc,
			NumEnums:      1,
			NumMessages:   0,
			NumExtensions: 0,
			NumServices:   0,
		},
		GoTypes:           file_google_type_calendar_period_proto_goTypes,
		DependencyIndexes: file_google_type_calendar_period_proto_depIdxs,
		EnumInfos:         file_google_type_calendar_period_proto_enumTypes,
	}.Build()
	File_google_type_calendar_period_proto = out.File
	file_google_type_calendar_period_proto_rawDesc = nil
	file_google_type_calendar_period_proto_goTypes = nil
	file_google_type_calendar_period_proto_depIdxs = nil
}